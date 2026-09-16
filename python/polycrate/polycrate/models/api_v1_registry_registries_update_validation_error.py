from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_registry_registries_update_annotations_error_component import (
        ApiV1RegistryRegistriesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_archived_at_error_component import (
        ApiV1RegistryRegistriesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_archived_error_component import (
        ApiV1RegistryRegistriesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_archived_reason_error_component import (
        ApiV1RegistryRegistriesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_credential_error_component import (
        ApiV1RegistryRegistriesUpdateCredentialErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_criticality_error_component import (
        ApiV1RegistryRegistriesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_debug_mode_error_component import (
        ApiV1RegistryRegistriesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_display_name_error_component import (
        ApiV1RegistryRegistriesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_hostname_error_component import (
        ApiV1RegistryRegistriesUpdateHostnameErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_k8s_app_error_component import (
        ApiV1RegistryRegistriesUpdateK8SAppErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_k8s_cluster_error_component import (
        ApiV1RegistryRegistriesUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_kind_error_component import (
        ApiV1RegistryRegistriesUpdateKindErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_labels_error_component import (
        ApiV1RegistryRegistriesUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_metadata_error_component import (
        ApiV1RegistryRegistriesUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_name_error_component import (
        ApiV1RegistryRegistriesUpdateNameErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_non_field_errors_error_component import (
        ApiV1RegistryRegistriesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_platform_service_error_component import (
        ApiV1RegistryRegistriesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_projects_count_error_component import (
        ApiV1RegistryRegistriesUpdateProjectsCountErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_provider_error_component import (
        ApiV1RegistryRegistriesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_provider_id_error_component import (
        ApiV1RegistryRegistriesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_provider_reference_error_component import (
        ApiV1RegistryRegistriesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_reconciliation_enabled_error_component import (
        ApiV1RegistryRegistriesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_registry_version_error_component import (
        ApiV1RegistryRegistriesUpdateRegistryVersionErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_repositories_count_error_component import (
        ApiV1RegistryRegistriesUpdateRepositoriesCountErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_sla_availability_error_component import (
        ApiV1RegistryRegistriesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_sla_target_error_component import (
        ApiV1RegistryRegistriesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_slo_availability_error_component import (
        ApiV1RegistryRegistriesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_slo_target_error_component import (
        ApiV1RegistryRegistriesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_storage_used_bytes_error_component import (
        ApiV1RegistryRegistriesUpdateStorageUsedBytesErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_target_availability_error_component import (
        ApiV1RegistryRegistriesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_registry_registries_update_tolerations_error_component import (
        ApiV1RegistryRegistriesUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1RegistryRegistriesUpdateValidationError")


@_attrs_define
class ApiV1RegistryRegistriesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1RegistryRegistriesUpdateAnnotationsErrorComponent |
            ApiV1RegistryRegistriesUpdateArchivedAtErrorComponent | ApiV1RegistryRegistriesUpdateArchivedErrorComponent |
            ApiV1RegistryRegistriesUpdateArchivedReasonErrorComponent |
            ApiV1RegistryRegistriesUpdateCredentialErrorComponent | ApiV1RegistryRegistriesUpdateCriticalityErrorComponent |
            ApiV1RegistryRegistriesUpdateDebugModeErrorComponent | ApiV1RegistryRegistriesUpdateDisplayNameErrorComponent |
            ApiV1RegistryRegistriesUpdateHostnameErrorComponent | ApiV1RegistryRegistriesUpdateK8SAppErrorComponent |
            ApiV1RegistryRegistriesUpdateK8SClusterErrorComponent | ApiV1RegistryRegistriesUpdateKindErrorComponent |
            ApiV1RegistryRegistriesUpdateLabelsErrorComponent | ApiV1RegistryRegistriesUpdateMetadataErrorComponent |
            ApiV1RegistryRegistriesUpdateNameErrorComponent | ApiV1RegistryRegistriesUpdateNonFieldErrorsErrorComponent |
            ApiV1RegistryRegistriesUpdatePlatformServiceErrorComponent |
            ApiV1RegistryRegistriesUpdateProjectsCountErrorComponent | ApiV1RegistryRegistriesUpdateProviderErrorComponent |
            ApiV1RegistryRegistriesUpdateProviderIdErrorComponent |
            ApiV1RegistryRegistriesUpdateProviderReferenceErrorComponent |
            ApiV1RegistryRegistriesUpdateReconciliationEnabledErrorComponent |
            ApiV1RegistryRegistriesUpdateRegistryVersionErrorComponent |
            ApiV1RegistryRegistriesUpdateRepositoriesCountErrorComponent |
            ApiV1RegistryRegistriesUpdateSlaAvailabilityErrorComponent |
            ApiV1RegistryRegistriesUpdateSlaTargetErrorComponent |
            ApiV1RegistryRegistriesUpdateSloAvailabilityErrorComponent |
            ApiV1RegistryRegistriesUpdateSloTargetErrorComponent |
            ApiV1RegistryRegistriesUpdateStorageUsedBytesErrorComponent |
            ApiV1RegistryRegistriesUpdateTargetAvailabilityErrorComponent |
            ApiV1RegistryRegistriesUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1RegistryRegistriesUpdateAnnotationsErrorComponent
        | ApiV1RegistryRegistriesUpdateArchivedAtErrorComponent
        | ApiV1RegistryRegistriesUpdateArchivedErrorComponent
        | ApiV1RegistryRegistriesUpdateArchivedReasonErrorComponent
        | ApiV1RegistryRegistriesUpdateCredentialErrorComponent
        | ApiV1RegistryRegistriesUpdateCriticalityErrorComponent
        | ApiV1RegistryRegistriesUpdateDebugModeErrorComponent
        | ApiV1RegistryRegistriesUpdateDisplayNameErrorComponent
        | ApiV1RegistryRegistriesUpdateHostnameErrorComponent
        | ApiV1RegistryRegistriesUpdateK8SAppErrorComponent
        | ApiV1RegistryRegistriesUpdateK8SClusterErrorComponent
        | ApiV1RegistryRegistriesUpdateKindErrorComponent
        | ApiV1RegistryRegistriesUpdateLabelsErrorComponent
        | ApiV1RegistryRegistriesUpdateMetadataErrorComponent
        | ApiV1RegistryRegistriesUpdateNameErrorComponent
        | ApiV1RegistryRegistriesUpdateNonFieldErrorsErrorComponent
        | ApiV1RegistryRegistriesUpdatePlatformServiceErrorComponent
        | ApiV1RegistryRegistriesUpdateProjectsCountErrorComponent
        | ApiV1RegistryRegistriesUpdateProviderErrorComponent
        | ApiV1RegistryRegistriesUpdateProviderIdErrorComponent
        | ApiV1RegistryRegistriesUpdateProviderReferenceErrorComponent
        | ApiV1RegistryRegistriesUpdateReconciliationEnabledErrorComponent
        | ApiV1RegistryRegistriesUpdateRegistryVersionErrorComponent
        | ApiV1RegistryRegistriesUpdateRepositoriesCountErrorComponent
        | ApiV1RegistryRegistriesUpdateSlaAvailabilityErrorComponent
        | ApiV1RegistryRegistriesUpdateSlaTargetErrorComponent
        | ApiV1RegistryRegistriesUpdateSloAvailabilityErrorComponent
        | ApiV1RegistryRegistriesUpdateSloTargetErrorComponent
        | ApiV1RegistryRegistriesUpdateStorageUsedBytesErrorComponent
        | ApiV1RegistryRegistriesUpdateTargetAvailabilityErrorComponent
        | ApiV1RegistryRegistriesUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_registry_registries_update_annotations_error_component import (
            ApiV1RegistryRegistriesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_archived_at_error_component import (
            ApiV1RegistryRegistriesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_archived_error_component import (
            ApiV1RegistryRegistriesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_archived_reason_error_component import (
            ApiV1RegistryRegistriesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_credential_error_component import (
            ApiV1RegistryRegistriesUpdateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_criticality_error_component import (
            ApiV1RegistryRegistriesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_debug_mode_error_component import (
            ApiV1RegistryRegistriesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_display_name_error_component import (
            ApiV1RegistryRegistriesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_hostname_error_component import (
            ApiV1RegistryRegistriesUpdateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_k8s_app_error_component import (
            ApiV1RegistryRegistriesUpdateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_k8s_cluster_error_component import (
            ApiV1RegistryRegistriesUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_kind_error_component import (
            ApiV1RegistryRegistriesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_labels_error_component import (
            ApiV1RegistryRegistriesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_name_error_component import (
            ApiV1RegistryRegistriesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_non_field_errors_error_component import (
            ApiV1RegistryRegistriesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_platform_service_error_component import (
            ApiV1RegistryRegistriesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_projects_count_error_component import (
            ApiV1RegistryRegistriesUpdateProjectsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_provider_error_component import (
            ApiV1RegistryRegistriesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_provider_id_error_component import (
            ApiV1RegistryRegistriesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_provider_reference_error_component import (
            ApiV1RegistryRegistriesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_reconciliation_enabled_error_component import (
            ApiV1RegistryRegistriesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_registry_version_error_component import (
            ApiV1RegistryRegistriesUpdateRegistryVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_repositories_count_error_component import (
            ApiV1RegistryRegistriesUpdateRepositoriesCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_sla_availability_error_component import (
            ApiV1RegistryRegistriesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_sla_target_error_component import (
            ApiV1RegistryRegistriesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_slo_availability_error_component import (
            ApiV1RegistryRegistriesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_slo_target_error_component import (
            ApiV1RegistryRegistriesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_storage_used_bytes_error_component import (
            ApiV1RegistryRegistriesUpdateStorageUsedBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_target_availability_error_component import (
            ApiV1RegistryRegistriesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_tolerations_error_component import (
            ApiV1RegistryRegistriesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateProjectsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateRepositoriesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateStorageUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateRegistryVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesUpdateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_registry_registries_update_annotations_error_component import (
            ApiV1RegistryRegistriesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_archived_at_error_component import (
            ApiV1RegistryRegistriesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_archived_error_component import (
            ApiV1RegistryRegistriesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_archived_reason_error_component import (
            ApiV1RegistryRegistriesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_credential_error_component import (
            ApiV1RegistryRegistriesUpdateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_criticality_error_component import (
            ApiV1RegistryRegistriesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_debug_mode_error_component import (
            ApiV1RegistryRegistriesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_display_name_error_component import (
            ApiV1RegistryRegistriesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_hostname_error_component import (
            ApiV1RegistryRegistriesUpdateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_k8s_app_error_component import (
            ApiV1RegistryRegistriesUpdateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_k8s_cluster_error_component import (
            ApiV1RegistryRegistriesUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_kind_error_component import (
            ApiV1RegistryRegistriesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_labels_error_component import (
            ApiV1RegistryRegistriesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_metadata_error_component import (
            ApiV1RegistryRegistriesUpdateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_name_error_component import (
            ApiV1RegistryRegistriesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_non_field_errors_error_component import (
            ApiV1RegistryRegistriesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_platform_service_error_component import (
            ApiV1RegistryRegistriesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_projects_count_error_component import (
            ApiV1RegistryRegistriesUpdateProjectsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_provider_error_component import (
            ApiV1RegistryRegistriesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_provider_id_error_component import (
            ApiV1RegistryRegistriesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_provider_reference_error_component import (
            ApiV1RegistryRegistriesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_reconciliation_enabled_error_component import (
            ApiV1RegistryRegistriesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_registry_version_error_component import (
            ApiV1RegistryRegistriesUpdateRegistryVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_repositories_count_error_component import (
            ApiV1RegistryRegistriesUpdateRepositoriesCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_sla_availability_error_component import (
            ApiV1RegistryRegistriesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_sla_target_error_component import (
            ApiV1RegistryRegistriesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_slo_availability_error_component import (
            ApiV1RegistryRegistriesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_slo_target_error_component import (
            ApiV1RegistryRegistriesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_storage_used_bytes_error_component import (
            ApiV1RegistryRegistriesUpdateStorageUsedBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_target_availability_error_component import (
            ApiV1RegistryRegistriesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_update_tolerations_error_component import (
            ApiV1RegistryRegistriesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1RegistryRegistriesUpdateAnnotationsErrorComponent
                | ApiV1RegistryRegistriesUpdateArchivedAtErrorComponent
                | ApiV1RegistryRegistriesUpdateArchivedErrorComponent
                | ApiV1RegistryRegistriesUpdateArchivedReasonErrorComponent
                | ApiV1RegistryRegistriesUpdateCredentialErrorComponent
                | ApiV1RegistryRegistriesUpdateCriticalityErrorComponent
                | ApiV1RegistryRegistriesUpdateDebugModeErrorComponent
                | ApiV1RegistryRegistriesUpdateDisplayNameErrorComponent
                | ApiV1RegistryRegistriesUpdateHostnameErrorComponent
                | ApiV1RegistryRegistriesUpdateK8SAppErrorComponent
                | ApiV1RegistryRegistriesUpdateK8SClusterErrorComponent
                | ApiV1RegistryRegistriesUpdateKindErrorComponent
                | ApiV1RegistryRegistriesUpdateLabelsErrorComponent
                | ApiV1RegistryRegistriesUpdateMetadataErrorComponent
                | ApiV1RegistryRegistriesUpdateNameErrorComponent
                | ApiV1RegistryRegistriesUpdateNonFieldErrorsErrorComponent
                | ApiV1RegistryRegistriesUpdatePlatformServiceErrorComponent
                | ApiV1RegistryRegistriesUpdateProjectsCountErrorComponent
                | ApiV1RegistryRegistriesUpdateProviderErrorComponent
                | ApiV1RegistryRegistriesUpdateProviderIdErrorComponent
                | ApiV1RegistryRegistriesUpdateProviderReferenceErrorComponent
                | ApiV1RegistryRegistriesUpdateReconciliationEnabledErrorComponent
                | ApiV1RegistryRegistriesUpdateRegistryVersionErrorComponent
                | ApiV1RegistryRegistriesUpdateRepositoriesCountErrorComponent
                | ApiV1RegistryRegistriesUpdateSlaAvailabilityErrorComponent
                | ApiV1RegistryRegistriesUpdateSlaTargetErrorComponent
                | ApiV1RegistryRegistriesUpdateSloAvailabilityErrorComponent
                | ApiV1RegistryRegistriesUpdateSloTargetErrorComponent
                | ApiV1RegistryRegistriesUpdateStorageUsedBytesErrorComponent
                | ApiV1RegistryRegistriesUpdateTargetAvailabilityErrorComponent
                | ApiV1RegistryRegistriesUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_0 = (
                        ApiV1RegistryRegistriesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_1 = (
                        ApiV1RegistryRegistriesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_2 = (
                        ApiV1RegistryRegistriesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_3 = (
                        ApiV1RegistryRegistriesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_4 = (
                        ApiV1RegistryRegistriesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_5 = (
                        ApiV1RegistryRegistriesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_6 = (
                        ApiV1RegistryRegistriesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_7 = (
                        ApiV1RegistryRegistriesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_8 = (
                        ApiV1RegistryRegistriesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_9 = (
                        ApiV1RegistryRegistriesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_10 = (
                        ApiV1RegistryRegistriesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_11 = (
                        ApiV1RegistryRegistriesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_12 = (
                        ApiV1RegistryRegistriesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_13 = (
                        ApiV1RegistryRegistriesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_14 = (
                        ApiV1RegistryRegistriesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_15 = (
                        ApiV1RegistryRegistriesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_16 = (
                        ApiV1RegistryRegistriesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_17 = (
                        ApiV1RegistryRegistriesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_18 = (
                        ApiV1RegistryRegistriesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_19 = (
                        ApiV1RegistryRegistriesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_20 = (
                        ApiV1RegistryRegistriesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_21 = (
                        ApiV1RegistryRegistriesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_22 = (
                        ApiV1RegistryRegistriesUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_23 = (
                        ApiV1RegistryRegistriesUpdateProjectsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_24 = (
                        ApiV1RegistryRegistriesUpdateRepositoriesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_25 = (
                        ApiV1RegistryRegistriesUpdateStorageUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_26 = (
                        ApiV1RegistryRegistriesUpdateRegistryVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_27 = (
                        ApiV1RegistryRegistriesUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_28 = (
                        ApiV1RegistryRegistriesUpdateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_update_error_type_29 = (
                        ApiV1RegistryRegistriesUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_registry_registries_update_error_type_30 = (
                    ApiV1RegistryRegistriesUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_registry_registries_update_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_registry_registries_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_registry_registries_update_validation_error.additional_properties = d
        return api_v1_registry_registries_update_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
