from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_secretmanager_managers_archive_create_annotations_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_archived_at_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_archived_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_archived_reason_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_auth_methods_count_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateAuthMethodsCountErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_credential_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateCredentialErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_criticality_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_debug_mode_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_display_name_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_hostname_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateHostnameErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_is_initialized_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateIsInitializedErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_is_sealed_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateIsSealedErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_k8s_app_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_k8s_cluster_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_kind_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_labels_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_metadata_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateMetadataErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_name_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_non_field_errors_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_platform_service_error_component import (
        ApiV1SecretmanagerManagersArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_policies_count_error_component import (
        ApiV1SecretmanagerManagersArchiveCreatePoliciesCountErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_provider_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_provider_id_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_provider_reference_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_reconciliation_enabled_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_secrets_engines_count_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateSecretsEnginesCountErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_sla_availability_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_sla_target_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_slo_availability_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_slo_target_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_target_availability_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_tolerations_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_vault_mode_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateVaultModeErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_archive_create_vault_version_error_component import (
        ApiV1SecretmanagerManagersArchiveCreateVaultVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1SecretmanagerManagersArchiveCreateValidationError")


@_attrs_define
class ApiV1SecretmanagerManagersArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1SecretmanagerManagersArchiveCreateAnnotationsErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateArchivedAtErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateArchivedErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateArchivedReasonErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateAuthMethodsCountErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateCredentialErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateCriticalityErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateDebugModeErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateDisplayNameErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateHostnameErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateIsInitializedErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateIsSealedErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateK8SAppErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateK8SClusterErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateKindErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateLabelsErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateMetadataErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateNameErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreatePlatformServiceErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreatePoliciesCountErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateProviderErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateProviderIdErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateProviderReferenceErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateSecretsEnginesCountErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateSlaTargetErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateSloAvailabilityErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateSloTargetErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateTolerationsErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateVaultModeErrorComponent |
            ApiV1SecretmanagerManagersArchiveCreateVaultVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1SecretmanagerManagersArchiveCreateAnnotationsErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateArchivedAtErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateArchivedErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateArchivedReasonErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateAuthMethodsCountErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateCredentialErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateCriticalityErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateDebugModeErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateDisplayNameErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateHostnameErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateIsInitializedErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateIsSealedErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateK8SAppErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateK8SClusterErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateKindErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateLabelsErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateMetadataErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateNameErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreatePlatformServiceErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreatePoliciesCountErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateProviderErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateProviderIdErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateProviderReferenceErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateSecretsEnginesCountErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateSlaTargetErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateSloAvailabilityErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateSloTargetErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateTolerationsErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateVaultModeErrorComponent
        | ApiV1SecretmanagerManagersArchiveCreateVaultVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_secretmanager_managers_archive_create_annotations_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_archived_at_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_archived_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_archived_reason_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_auth_methods_count_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateAuthMethodsCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_credential_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateCredentialErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_criticality_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_debug_mode_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_display_name_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_hostname_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateHostnameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_is_initialized_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateIsInitializedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_is_sealed_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateIsSealedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_k8s_app_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_k8s_cluster_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_kind_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_labels_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_name_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_non_field_errors_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_platform_service_error_component import (
            ApiV1SecretmanagerManagersArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_policies_count_error_component import (
            ApiV1SecretmanagerManagersArchiveCreatePoliciesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_provider_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_provider_id_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_provider_reference_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_reconciliation_enabled_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_secrets_engines_count_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateSecretsEnginesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_sla_availability_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_sla_target_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_slo_availability_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_slo_target_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_target_availability_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_tolerations_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_vault_mode_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateVaultModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_vault_version_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateVaultVersionErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1SecretmanagerManagersArchiveCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateVaultModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateIsSealedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateIsInitializedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateSecretsEnginesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateAuthMethodsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreatePoliciesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateVaultVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersArchiveCreateCredentialErrorComponent):
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
        from ..models.api_v1_secretmanager_managers_archive_create_annotations_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_archived_at_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_archived_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_archived_reason_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_auth_methods_count_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateAuthMethodsCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_credential_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateCredentialErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_criticality_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_debug_mode_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_display_name_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_hostname_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateHostnameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_is_initialized_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateIsInitializedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_is_sealed_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateIsSealedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_k8s_app_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_k8s_cluster_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_kind_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_labels_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_metadata_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateMetadataErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_name_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_non_field_errors_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_platform_service_error_component import (
            ApiV1SecretmanagerManagersArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_policies_count_error_component import (
            ApiV1SecretmanagerManagersArchiveCreatePoliciesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_provider_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_provider_id_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_provider_reference_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_reconciliation_enabled_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_secrets_engines_count_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateSecretsEnginesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_sla_availability_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_sla_target_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_slo_availability_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_slo_target_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_target_availability_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_tolerations_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_vault_mode_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateVaultModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_archive_create_vault_version_error_component import (
            ApiV1SecretmanagerManagersArchiveCreateVaultVersionErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1SecretmanagerManagersArchiveCreateAnnotationsErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateArchivedAtErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateArchivedErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateArchivedReasonErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateAuthMethodsCountErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateCredentialErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateCriticalityErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateDebugModeErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateDisplayNameErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateHostnameErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateIsInitializedErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateIsSealedErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateK8SAppErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateK8SClusterErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateKindErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateLabelsErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateMetadataErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateNameErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreatePlatformServiceErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreatePoliciesCountErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateProviderErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateProviderIdErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateProviderReferenceErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateSecretsEnginesCountErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateSlaTargetErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateSloAvailabilityErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateSloTargetErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateTolerationsErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateVaultModeErrorComponent
                | ApiV1SecretmanagerManagersArchiveCreateVaultVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_0 = (
                        ApiV1SecretmanagerManagersArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_1 = (
                        ApiV1SecretmanagerManagersArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_2 = (
                        ApiV1SecretmanagerManagersArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_3 = (
                        ApiV1SecretmanagerManagersArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_4 = (
                        ApiV1SecretmanagerManagersArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_5 = (
                        ApiV1SecretmanagerManagersArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_6 = (
                        ApiV1SecretmanagerManagersArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_7 = (
                        ApiV1SecretmanagerManagersArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_8 = (
                        ApiV1SecretmanagerManagersArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_9 = (
                        ApiV1SecretmanagerManagersArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_10 = (
                        ApiV1SecretmanagerManagersArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_11 = (
                        ApiV1SecretmanagerManagersArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_12 = (
                        ApiV1SecretmanagerManagersArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_13 = (
                        ApiV1SecretmanagerManagersArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_14 = (
                        ApiV1SecretmanagerManagersArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_15 = (
                        ApiV1SecretmanagerManagersArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_16 = (
                        ApiV1SecretmanagerManagersArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_17 = (
                        ApiV1SecretmanagerManagersArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_18 = (
                        ApiV1SecretmanagerManagersArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_19 = (
                        ApiV1SecretmanagerManagersArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_20 = (
                        ApiV1SecretmanagerManagersArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_21 = (
                        ApiV1SecretmanagerManagersArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_22 = (
                        ApiV1SecretmanagerManagersArchiveCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_23 = (
                        ApiV1SecretmanagerManagersArchiveCreateVaultModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_24 = (
                        ApiV1SecretmanagerManagersArchiveCreateIsSealedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_25 = (
                        ApiV1SecretmanagerManagersArchiveCreateIsInitializedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_26 = (
                        ApiV1SecretmanagerManagersArchiveCreateSecretsEnginesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_27 = (
                        ApiV1SecretmanagerManagersArchiveCreateAuthMethodsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_28 = (
                        ApiV1SecretmanagerManagersArchiveCreatePoliciesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_29 = (
                        ApiV1SecretmanagerManagersArchiveCreateVaultVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_30 = (
                        ApiV1SecretmanagerManagersArchiveCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_31 = (
                        ApiV1SecretmanagerManagersArchiveCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_32 = (
                        ApiV1SecretmanagerManagersArchiveCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_33 = (
                    ApiV1SecretmanagerManagersArchiveCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_secretmanager_managers_archive_create_error_type_33

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_secretmanager_managers_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_secretmanager_managers_archive_create_validation_error.additional_properties = d
        return api_v1_secretmanager_managers_archive_create_validation_error

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
