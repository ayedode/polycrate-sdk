from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_registry_registries_create_annotations_error_component import (
        ApiV1RegistryRegistriesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_archived_at_error_component import (
        ApiV1RegistryRegistriesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_archived_error_component import (
        ApiV1RegistryRegistriesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_archived_reason_error_component import (
        ApiV1RegistryRegistriesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_credential_error_component import (
        ApiV1RegistryRegistriesCreateCredentialErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_criticality_error_component import (
        ApiV1RegistryRegistriesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_debug_mode_error_component import (
        ApiV1RegistryRegistriesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_display_name_error_component import (
        ApiV1RegistryRegistriesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_hostname_error_component import (
        ApiV1RegistryRegistriesCreateHostnameErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_k8s_app_error_component import (
        ApiV1RegistryRegistriesCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_k8s_cluster_error_component import (
        ApiV1RegistryRegistriesCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_kind_error_component import (
        ApiV1RegistryRegistriesCreateKindErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_labels_error_component import (
        ApiV1RegistryRegistriesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_metadata_error_component import (
        ApiV1RegistryRegistriesCreateMetadataErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_name_error_component import (
        ApiV1RegistryRegistriesCreateNameErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_non_field_errors_error_component import (
        ApiV1RegistryRegistriesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_platform_service_error_component import (
        ApiV1RegistryRegistriesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_projects_count_error_component import (
        ApiV1RegistryRegistriesCreateProjectsCountErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_provider_error_component import (
        ApiV1RegistryRegistriesCreateProviderErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_provider_id_error_component import (
        ApiV1RegistryRegistriesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_provider_reference_error_component import (
        ApiV1RegistryRegistriesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_reconciliation_enabled_error_component import (
        ApiV1RegistryRegistriesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_registry_version_error_component import (
        ApiV1RegistryRegistriesCreateRegistryVersionErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_repositories_count_error_component import (
        ApiV1RegistryRegistriesCreateRepositoriesCountErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_sla_availability_error_component import (
        ApiV1RegistryRegistriesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_sla_target_error_component import (
        ApiV1RegistryRegistriesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_slo_availability_error_component import (
        ApiV1RegistryRegistriesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_slo_target_error_component import (
        ApiV1RegistryRegistriesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_storage_used_bytes_error_component import (
        ApiV1RegistryRegistriesCreateStorageUsedBytesErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_target_availability_error_component import (
        ApiV1RegistryRegistriesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_registry_registries_create_tolerations_error_component import (
        ApiV1RegistryRegistriesCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1RegistryRegistriesCreateValidationError")


@_attrs_define
class ApiV1RegistryRegistriesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1RegistryRegistriesCreateAnnotationsErrorComponent |
            ApiV1RegistryRegistriesCreateArchivedAtErrorComponent | ApiV1RegistryRegistriesCreateArchivedErrorComponent |
            ApiV1RegistryRegistriesCreateArchivedReasonErrorComponent |
            ApiV1RegistryRegistriesCreateCredentialErrorComponent | ApiV1RegistryRegistriesCreateCriticalityErrorComponent |
            ApiV1RegistryRegistriesCreateDebugModeErrorComponent | ApiV1RegistryRegistriesCreateDisplayNameErrorComponent |
            ApiV1RegistryRegistriesCreateHostnameErrorComponent | ApiV1RegistryRegistriesCreateK8SAppErrorComponent |
            ApiV1RegistryRegistriesCreateK8SClusterErrorComponent | ApiV1RegistryRegistriesCreateKindErrorComponent |
            ApiV1RegistryRegistriesCreateLabelsErrorComponent | ApiV1RegistryRegistriesCreateMetadataErrorComponent |
            ApiV1RegistryRegistriesCreateNameErrorComponent | ApiV1RegistryRegistriesCreateNonFieldErrorsErrorComponent |
            ApiV1RegistryRegistriesCreatePlatformServiceErrorComponent |
            ApiV1RegistryRegistriesCreateProjectsCountErrorComponent | ApiV1RegistryRegistriesCreateProviderErrorComponent |
            ApiV1RegistryRegistriesCreateProviderIdErrorComponent |
            ApiV1RegistryRegistriesCreateProviderReferenceErrorComponent |
            ApiV1RegistryRegistriesCreateReconciliationEnabledErrorComponent |
            ApiV1RegistryRegistriesCreateRegistryVersionErrorComponent |
            ApiV1RegistryRegistriesCreateRepositoriesCountErrorComponent |
            ApiV1RegistryRegistriesCreateSlaAvailabilityErrorComponent |
            ApiV1RegistryRegistriesCreateSlaTargetErrorComponent |
            ApiV1RegistryRegistriesCreateSloAvailabilityErrorComponent |
            ApiV1RegistryRegistriesCreateSloTargetErrorComponent |
            ApiV1RegistryRegistriesCreateStorageUsedBytesErrorComponent |
            ApiV1RegistryRegistriesCreateTargetAvailabilityErrorComponent |
            ApiV1RegistryRegistriesCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1RegistryRegistriesCreateAnnotationsErrorComponent
        | ApiV1RegistryRegistriesCreateArchivedAtErrorComponent
        | ApiV1RegistryRegistriesCreateArchivedErrorComponent
        | ApiV1RegistryRegistriesCreateArchivedReasonErrorComponent
        | ApiV1RegistryRegistriesCreateCredentialErrorComponent
        | ApiV1RegistryRegistriesCreateCriticalityErrorComponent
        | ApiV1RegistryRegistriesCreateDebugModeErrorComponent
        | ApiV1RegistryRegistriesCreateDisplayNameErrorComponent
        | ApiV1RegistryRegistriesCreateHostnameErrorComponent
        | ApiV1RegistryRegistriesCreateK8SAppErrorComponent
        | ApiV1RegistryRegistriesCreateK8SClusterErrorComponent
        | ApiV1RegistryRegistriesCreateKindErrorComponent
        | ApiV1RegistryRegistriesCreateLabelsErrorComponent
        | ApiV1RegistryRegistriesCreateMetadataErrorComponent
        | ApiV1RegistryRegistriesCreateNameErrorComponent
        | ApiV1RegistryRegistriesCreateNonFieldErrorsErrorComponent
        | ApiV1RegistryRegistriesCreatePlatformServiceErrorComponent
        | ApiV1RegistryRegistriesCreateProjectsCountErrorComponent
        | ApiV1RegistryRegistriesCreateProviderErrorComponent
        | ApiV1RegistryRegistriesCreateProviderIdErrorComponent
        | ApiV1RegistryRegistriesCreateProviderReferenceErrorComponent
        | ApiV1RegistryRegistriesCreateReconciliationEnabledErrorComponent
        | ApiV1RegistryRegistriesCreateRegistryVersionErrorComponent
        | ApiV1RegistryRegistriesCreateRepositoriesCountErrorComponent
        | ApiV1RegistryRegistriesCreateSlaAvailabilityErrorComponent
        | ApiV1RegistryRegistriesCreateSlaTargetErrorComponent
        | ApiV1RegistryRegistriesCreateSloAvailabilityErrorComponent
        | ApiV1RegistryRegistriesCreateSloTargetErrorComponent
        | ApiV1RegistryRegistriesCreateStorageUsedBytesErrorComponent
        | ApiV1RegistryRegistriesCreateTargetAvailabilityErrorComponent
        | ApiV1RegistryRegistriesCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_registry_registries_create_annotations_error_component import (
            ApiV1RegistryRegistriesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_archived_at_error_component import (
            ApiV1RegistryRegistriesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_archived_error_component import (
            ApiV1RegistryRegistriesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_archived_reason_error_component import (
            ApiV1RegistryRegistriesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_credential_error_component import (
            ApiV1RegistryRegistriesCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_criticality_error_component import (
            ApiV1RegistryRegistriesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_debug_mode_error_component import (
            ApiV1RegistryRegistriesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_display_name_error_component import (
            ApiV1RegistryRegistriesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_hostname_error_component import (
            ApiV1RegistryRegistriesCreateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_k8s_app_error_component import (
            ApiV1RegistryRegistriesCreateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_k8s_cluster_error_component import (
            ApiV1RegistryRegistriesCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_kind_error_component import (
            ApiV1RegistryRegistriesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_labels_error_component import (
            ApiV1RegistryRegistriesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_name_error_component import (
            ApiV1RegistryRegistriesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_non_field_errors_error_component import (
            ApiV1RegistryRegistriesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_platform_service_error_component import (
            ApiV1RegistryRegistriesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_projects_count_error_component import (
            ApiV1RegistryRegistriesCreateProjectsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_provider_error_component import (
            ApiV1RegistryRegistriesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_provider_id_error_component import (
            ApiV1RegistryRegistriesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_provider_reference_error_component import (
            ApiV1RegistryRegistriesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_reconciliation_enabled_error_component import (
            ApiV1RegistryRegistriesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_registry_version_error_component import (
            ApiV1RegistryRegistriesCreateRegistryVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_repositories_count_error_component import (
            ApiV1RegistryRegistriesCreateRepositoriesCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_sla_availability_error_component import (
            ApiV1RegistryRegistriesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_sla_target_error_component import (
            ApiV1RegistryRegistriesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_slo_availability_error_component import (
            ApiV1RegistryRegistriesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_slo_target_error_component import (
            ApiV1RegistryRegistriesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_storage_used_bytes_error_component import (
            ApiV1RegistryRegistriesCreateStorageUsedBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_target_availability_error_component import (
            ApiV1RegistryRegistriesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_tolerations_error_component import (
            ApiV1RegistryRegistriesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1RegistryRegistriesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateProjectsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateRepositoriesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateStorageUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateRegistryVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegistryRegistriesCreateCredentialErrorComponent):
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
        from ..models.api_v1_registry_registries_create_annotations_error_component import (
            ApiV1RegistryRegistriesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_archived_at_error_component import (
            ApiV1RegistryRegistriesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_archived_error_component import (
            ApiV1RegistryRegistriesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_archived_reason_error_component import (
            ApiV1RegistryRegistriesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_credential_error_component import (
            ApiV1RegistryRegistriesCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_criticality_error_component import (
            ApiV1RegistryRegistriesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_debug_mode_error_component import (
            ApiV1RegistryRegistriesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_display_name_error_component import (
            ApiV1RegistryRegistriesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_hostname_error_component import (
            ApiV1RegistryRegistriesCreateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_k8s_app_error_component import (
            ApiV1RegistryRegistriesCreateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_k8s_cluster_error_component import (
            ApiV1RegistryRegistriesCreateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_kind_error_component import (
            ApiV1RegistryRegistriesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_labels_error_component import (
            ApiV1RegistryRegistriesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_metadata_error_component import (
            ApiV1RegistryRegistriesCreateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_name_error_component import (
            ApiV1RegistryRegistriesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_non_field_errors_error_component import (
            ApiV1RegistryRegistriesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_platform_service_error_component import (
            ApiV1RegistryRegistriesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_projects_count_error_component import (
            ApiV1RegistryRegistriesCreateProjectsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_provider_error_component import (
            ApiV1RegistryRegistriesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_provider_id_error_component import (
            ApiV1RegistryRegistriesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_provider_reference_error_component import (
            ApiV1RegistryRegistriesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_reconciliation_enabled_error_component import (
            ApiV1RegistryRegistriesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_registry_version_error_component import (
            ApiV1RegistryRegistriesCreateRegistryVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_repositories_count_error_component import (
            ApiV1RegistryRegistriesCreateRepositoriesCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_sla_availability_error_component import (
            ApiV1RegistryRegistriesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_sla_target_error_component import (
            ApiV1RegistryRegistriesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_slo_availability_error_component import (
            ApiV1RegistryRegistriesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_slo_target_error_component import (
            ApiV1RegistryRegistriesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_storage_used_bytes_error_component import (
            ApiV1RegistryRegistriesCreateStorageUsedBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_target_availability_error_component import (
            ApiV1RegistryRegistriesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_registry_registries_create_tolerations_error_component import (
            ApiV1RegistryRegistriesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1RegistryRegistriesCreateAnnotationsErrorComponent
                | ApiV1RegistryRegistriesCreateArchivedAtErrorComponent
                | ApiV1RegistryRegistriesCreateArchivedErrorComponent
                | ApiV1RegistryRegistriesCreateArchivedReasonErrorComponent
                | ApiV1RegistryRegistriesCreateCredentialErrorComponent
                | ApiV1RegistryRegistriesCreateCriticalityErrorComponent
                | ApiV1RegistryRegistriesCreateDebugModeErrorComponent
                | ApiV1RegistryRegistriesCreateDisplayNameErrorComponent
                | ApiV1RegistryRegistriesCreateHostnameErrorComponent
                | ApiV1RegistryRegistriesCreateK8SAppErrorComponent
                | ApiV1RegistryRegistriesCreateK8SClusterErrorComponent
                | ApiV1RegistryRegistriesCreateKindErrorComponent
                | ApiV1RegistryRegistriesCreateLabelsErrorComponent
                | ApiV1RegistryRegistriesCreateMetadataErrorComponent
                | ApiV1RegistryRegistriesCreateNameErrorComponent
                | ApiV1RegistryRegistriesCreateNonFieldErrorsErrorComponent
                | ApiV1RegistryRegistriesCreatePlatformServiceErrorComponent
                | ApiV1RegistryRegistriesCreateProjectsCountErrorComponent
                | ApiV1RegistryRegistriesCreateProviderErrorComponent
                | ApiV1RegistryRegistriesCreateProviderIdErrorComponent
                | ApiV1RegistryRegistriesCreateProviderReferenceErrorComponent
                | ApiV1RegistryRegistriesCreateReconciliationEnabledErrorComponent
                | ApiV1RegistryRegistriesCreateRegistryVersionErrorComponent
                | ApiV1RegistryRegistriesCreateRepositoriesCountErrorComponent
                | ApiV1RegistryRegistriesCreateSlaAvailabilityErrorComponent
                | ApiV1RegistryRegistriesCreateSlaTargetErrorComponent
                | ApiV1RegistryRegistriesCreateSloAvailabilityErrorComponent
                | ApiV1RegistryRegistriesCreateSloTargetErrorComponent
                | ApiV1RegistryRegistriesCreateStorageUsedBytesErrorComponent
                | ApiV1RegistryRegistriesCreateTargetAvailabilityErrorComponent
                | ApiV1RegistryRegistriesCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_0 = (
                        ApiV1RegistryRegistriesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_1 = (
                        ApiV1RegistryRegistriesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_2 = (
                        ApiV1RegistryRegistriesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_3 = (
                        ApiV1RegistryRegistriesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_4 = (
                        ApiV1RegistryRegistriesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_5 = (
                        ApiV1RegistryRegistriesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_6 = (
                        ApiV1RegistryRegistriesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_7 = (
                        ApiV1RegistryRegistriesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_8 = (
                        ApiV1RegistryRegistriesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_9 = (
                        ApiV1RegistryRegistriesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_10 = (
                        ApiV1RegistryRegistriesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_11 = (
                        ApiV1RegistryRegistriesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_12 = (
                        ApiV1RegistryRegistriesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_13 = (
                        ApiV1RegistryRegistriesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_14 = (
                        ApiV1RegistryRegistriesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_15 = (
                        ApiV1RegistryRegistriesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_16 = (
                        ApiV1RegistryRegistriesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_17 = (
                        ApiV1RegistryRegistriesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_18 = (
                        ApiV1RegistryRegistriesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_19 = (
                        ApiV1RegistryRegistriesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_20 = (
                        ApiV1RegistryRegistriesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_21 = (
                        ApiV1RegistryRegistriesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_22 = (
                        ApiV1RegistryRegistriesCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_23 = (
                        ApiV1RegistryRegistriesCreateProjectsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_24 = (
                        ApiV1RegistryRegistriesCreateRepositoriesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_25 = (
                        ApiV1RegistryRegistriesCreateStorageUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_26 = (
                        ApiV1RegistryRegistriesCreateRegistryVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_27 = (
                        ApiV1RegistryRegistriesCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_28 = (
                        ApiV1RegistryRegistriesCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_registry_registries_create_error_type_29 = (
                        ApiV1RegistryRegistriesCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_registry_registries_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_registry_registries_create_error_type_30 = (
                    ApiV1RegistryRegistriesCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_registry_registries_create_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_registry_registries_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_registry_registries_create_validation_error.additional_properties = d
        return api_v1_registry_registries_create_validation_error

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
