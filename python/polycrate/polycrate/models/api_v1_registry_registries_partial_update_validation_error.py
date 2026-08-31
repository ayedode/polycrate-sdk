from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_registry_registries_partial_update_annotations_error_component import (
        ApiV1RegistryRegistriesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_archived_at_error_component import (
        ApiV1RegistryRegistriesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_archived_error_component import (
        ApiV1RegistryRegistriesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_archived_reason_error_component import (
        ApiV1RegistryRegistriesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_credential_error_component import (
        ApiV1RegistryRegistriesPartialUpdateCredentialErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_criticality_error_component import (
        ApiV1RegistryRegistriesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_debug_mode_error_component import (
        ApiV1RegistryRegistriesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_display_name_error_component import (
        ApiV1RegistryRegistriesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_hostname_error_component import (
        ApiV1RegistryRegistriesPartialUpdateHostnameErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_k8s_app_error_component import (
        ApiV1RegistryRegistriesPartialUpdateK8SAppErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_k8s_cluster_error_component import (
        ApiV1RegistryRegistriesPartialUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_kind_error_component import (
        ApiV1RegistryRegistriesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_labels_error_component import (
        ApiV1RegistryRegistriesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_metadata_error_component import (
        ApiV1RegistryRegistriesPartialUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_name_error_component import (
        ApiV1RegistryRegistriesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_non_field_errors_error_component import (
        ApiV1RegistryRegistriesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_platform_service_error_component import (
        ApiV1RegistryRegistriesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_projects_count_error_component import (
        ApiV1RegistryRegistriesPartialUpdateProjectsCountErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_provider_error_component import (
        ApiV1RegistryRegistriesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_provider_id_error_component import (
        ApiV1RegistryRegistriesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_provider_reference_error_component import (
        ApiV1RegistryRegistriesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_reconciliation_enabled_error_component import (
        ApiV1RegistryRegistriesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_registry_version_error_component import (
        ApiV1RegistryRegistriesPartialUpdateRegistryVersionErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_repositories_count_error_component import (
        ApiV1RegistryRegistriesPartialUpdateRepositoriesCountErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_sla_availability_error_component import (
        ApiV1RegistryRegistriesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_sla_target_error_component import (
        ApiV1RegistryRegistriesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_slo_availability_error_component import (
        ApiV1RegistryRegistriesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_slo_target_error_component import (
        ApiV1RegistryRegistriesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_storage_used_bytes_error_component import (
        ApiV1RegistryRegistriesPartialUpdateStorageUsedBytesErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_target_availability_error_component import (
        ApiV1RegistryRegistriesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_registry_registries_partial_update_tolerations_error_component import (
        ApiV1RegistryRegistriesPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1RegistryRegistriesPartialUpdateValidationError")


@_attrs_define
class ApiV1RegistryRegistriesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1RegistryRegistriesPartialUpdateAnnotationsErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateArchivedAtErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateArchivedErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateArchivedReasonErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateCredentialErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateCriticalityErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateDebugModeErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateDisplayNameErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateHostnameErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateK8SAppErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateK8SClusterErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateKindErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateLabelsErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateMetadataErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateNameErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1RegistryRegistriesPartialUpdatePlatformServiceErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateProjectsCountErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateProviderErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateProviderIdErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateProviderReferenceErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateRegistryVersionErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateRepositoriesCountErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateSlaTargetErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateSloTargetErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateStorageUsedBytesErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1RegistryRegistriesPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1RegistryRegistriesPartialUpdateAnnotationsErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateArchivedAtErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateArchivedErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateArchivedReasonErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateCredentialErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateCriticalityErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateDebugModeErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateDisplayNameErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateHostnameErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateK8SAppErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateK8SClusterErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateKindErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateLabelsErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateMetadataErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateNameErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1RegistryRegistriesPartialUpdatePlatformServiceErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateProjectsCountErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateProviderErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateProviderIdErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateProviderReferenceErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateRegistryVersionErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateRepositoriesCountErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateSlaTargetErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateSloTargetErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateStorageUsedBytesErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1RegistryRegistriesPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_registry_registries_partial_update_annotations_error_component import (
            ApiV1RegistryRegistriesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_archived_at_error_component import (
            ApiV1RegistryRegistriesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_archived_error_component import (
            ApiV1RegistryRegistriesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_archived_reason_error_component import (
            ApiV1RegistryRegistriesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_credential_error_component import (
            ApiV1RegistryRegistriesPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_criticality_error_component import (
            ApiV1RegistryRegistriesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_debug_mode_error_component import (
            ApiV1RegistryRegistriesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_display_name_error_component import (
            ApiV1RegistryRegistriesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_hostname_error_component import (
            ApiV1RegistryRegistriesPartialUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_k8s_app_error_component import (
            ApiV1RegistryRegistriesPartialUpdateK8SAppErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_k8s_cluster_error_component import (
            ApiV1RegistryRegistriesPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_kind_error_component import (
            ApiV1RegistryRegistriesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_labels_error_component import (
            ApiV1RegistryRegistriesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_name_error_component import (
            ApiV1RegistryRegistriesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_non_field_errors_error_component import (
            ApiV1RegistryRegistriesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_platform_service_error_component import (
            ApiV1RegistryRegistriesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_projects_count_error_component import (
            ApiV1RegistryRegistriesPartialUpdateProjectsCountErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_provider_error_component import (
            ApiV1RegistryRegistriesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_provider_id_error_component import (
            ApiV1RegistryRegistriesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_provider_reference_error_component import (
            ApiV1RegistryRegistriesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_reconciliation_enabled_error_component import (
            ApiV1RegistryRegistriesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_registry_version_error_component import (
            ApiV1RegistryRegistriesPartialUpdateRegistryVersionErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_repositories_count_error_component import (
            ApiV1RegistryRegistriesPartialUpdateRepositoriesCountErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_sla_availability_error_component import (
            ApiV1RegistryRegistriesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_sla_target_error_component import (
            ApiV1RegistryRegistriesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_slo_availability_error_component import (
            ApiV1RegistryRegistriesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_slo_target_error_component import (
            ApiV1RegistryRegistriesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_storage_used_bytes_error_component import (
            ApiV1RegistryRegistriesPartialUpdateStorageUsedBytesErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_target_availability_error_component import (
            ApiV1RegistryRegistriesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_tolerations_error_component import (
            ApiV1RegistryRegistriesPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateProjectsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateRepositoriesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateStorageUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateRegistryVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesPartialUpdateCredentialErrorComponent):
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
        from ..models.api_v1_registry_registries_partial_update_annotations_error_component import (
            ApiV1RegistryRegistriesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_archived_at_error_component import (
            ApiV1RegistryRegistriesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_archived_error_component import (
            ApiV1RegistryRegistriesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_archived_reason_error_component import (
            ApiV1RegistryRegistriesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_credential_error_component import (
            ApiV1RegistryRegistriesPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_criticality_error_component import (
            ApiV1RegistryRegistriesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_debug_mode_error_component import (
            ApiV1RegistryRegistriesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_display_name_error_component import (
            ApiV1RegistryRegistriesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_hostname_error_component import (
            ApiV1RegistryRegistriesPartialUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_k8s_app_error_component import (
            ApiV1RegistryRegistriesPartialUpdateK8SAppErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_k8s_cluster_error_component import (
            ApiV1RegistryRegistriesPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_kind_error_component import (
            ApiV1RegistryRegistriesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_labels_error_component import (
            ApiV1RegistryRegistriesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_metadata_error_component import (
            ApiV1RegistryRegistriesPartialUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_name_error_component import (
            ApiV1RegistryRegistriesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_non_field_errors_error_component import (
            ApiV1RegistryRegistriesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_platform_service_error_component import (
            ApiV1RegistryRegistriesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_projects_count_error_component import (
            ApiV1RegistryRegistriesPartialUpdateProjectsCountErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_provider_error_component import (
            ApiV1RegistryRegistriesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_provider_id_error_component import (
            ApiV1RegistryRegistriesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_provider_reference_error_component import (
            ApiV1RegistryRegistriesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_reconciliation_enabled_error_component import (
            ApiV1RegistryRegistriesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_registry_version_error_component import (
            ApiV1RegistryRegistriesPartialUpdateRegistryVersionErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_repositories_count_error_component import (
            ApiV1RegistryRegistriesPartialUpdateRepositoriesCountErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_sla_availability_error_component import (
            ApiV1RegistryRegistriesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_sla_target_error_component import (
            ApiV1RegistryRegistriesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_slo_availability_error_component import (
            ApiV1RegistryRegistriesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_slo_target_error_component import (
            ApiV1RegistryRegistriesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_storage_used_bytes_error_component import (
            ApiV1RegistryRegistriesPartialUpdateStorageUsedBytesErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_target_availability_error_component import (
            ApiV1RegistryRegistriesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_registry_registries_partial_update_tolerations_error_component import (
            ApiV1RegistryRegistriesPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1RegistryRegistriesPartialUpdateAnnotationsErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateArchivedAtErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateArchivedErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateArchivedReasonErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateCredentialErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateCriticalityErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateDebugModeErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateDisplayNameErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateHostnameErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateK8SAppErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateK8SClusterErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateKindErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateLabelsErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateMetadataErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateNameErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1RegistryRegistriesPartialUpdatePlatformServiceErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateProjectsCountErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateProviderErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateProviderIdErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateProviderReferenceErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateRegistryVersionErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateRepositoriesCountErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateSlaTargetErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateSloTargetErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateStorageUsedBytesErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1RegistryRegistriesPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_0 = (
                        ApiV1RegistryRegistriesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_1 = (
                        ApiV1RegistryRegistriesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_2 = (
                        ApiV1RegistryRegistriesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_3 = (
                        ApiV1RegistryRegistriesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_4 = (
                        ApiV1RegistryRegistriesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_5 = (
                        ApiV1RegistryRegistriesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_6 = (
                        ApiV1RegistryRegistriesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_7 = (
                        ApiV1RegistryRegistriesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_8 = (
                        ApiV1RegistryRegistriesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_9 = (
                        ApiV1RegistryRegistriesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_10 = (
                        ApiV1RegistryRegistriesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_11 = (
                        ApiV1RegistryRegistriesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_12 = (
                        ApiV1RegistryRegistriesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_13 = (
                        ApiV1RegistryRegistriesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_14 = (
                        ApiV1RegistryRegistriesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_15 = (
                        ApiV1RegistryRegistriesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_16 = (
                        ApiV1RegistryRegistriesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_17 = (
                        ApiV1RegistryRegistriesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_18 = (
                        ApiV1RegistryRegistriesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_19 = (
                        ApiV1RegistryRegistriesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_20 = (
                        ApiV1RegistryRegistriesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_21 = (
                        ApiV1RegistryRegistriesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_22 = (
                        ApiV1RegistryRegistriesPartialUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_23 = (
                        ApiV1RegistryRegistriesPartialUpdateProjectsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_24 = (
                        ApiV1RegistryRegistriesPartialUpdateRepositoriesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_25 = (
                        ApiV1RegistryRegistriesPartialUpdateStorageUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_26 = (
                        ApiV1RegistryRegistriesPartialUpdateRegistryVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_27 = (
                        ApiV1RegistryRegistriesPartialUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_28 = (
                        ApiV1RegistryRegistriesPartialUpdateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_partial_update_error_type_29 = (
                        ApiV1RegistryRegistriesPartialUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_registry_registries_partial_update_error_type_30 = (
                    ApiV1RegistryRegistriesPartialUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_registry_registries_partial_update_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_registry_registries_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_registry_registries_partial_update_validation_error.additional_properties = d
        return api_v1_registry_registries_partial_update_validation_error

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
