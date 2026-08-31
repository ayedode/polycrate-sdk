from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_secretmanager_managers_create_annotations_error_component import (
        ApiV1SecretmanagerManagersCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_archived_at_error_component import (
        ApiV1SecretmanagerManagersCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_archived_error_component import (
        ApiV1SecretmanagerManagersCreateArchivedErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_archived_reason_error_component import (
        ApiV1SecretmanagerManagersCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_auth_methods_count_error_component import (
        ApiV1SecretmanagerManagersCreateAuthMethodsCountErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_credential_error_component import (
        ApiV1SecretmanagerManagersCreateCredentialErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_criticality_error_component import (
        ApiV1SecretmanagerManagersCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_debug_mode_error_component import (
        ApiV1SecretmanagerManagersCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_display_name_error_component import (
        ApiV1SecretmanagerManagersCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_hostname_error_component import (
        ApiV1SecretmanagerManagersCreateHostnameErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_is_initialized_error_component import (
        ApiV1SecretmanagerManagersCreateIsInitializedErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_is_sealed_error_component import (
        ApiV1SecretmanagerManagersCreateIsSealedErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_k8s_app_error_component import (
        ApiV1SecretmanagerManagersCreateK8SAppErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_k8s_cluster_error_component import (
        ApiV1SecretmanagerManagersCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_kind_error_component import (
        ApiV1SecretmanagerManagersCreateKindErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_labels_error_component import (
        ApiV1SecretmanagerManagersCreateLabelsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_metadata_error_component import (
        ApiV1SecretmanagerManagersCreateMetadataErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_name_error_component import (
        ApiV1SecretmanagerManagersCreateNameErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_non_field_errors_error_component import (
        ApiV1SecretmanagerManagersCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_platform_service_error_component import (
        ApiV1SecretmanagerManagersCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_policies_count_error_component import (
        ApiV1SecretmanagerManagersCreatePoliciesCountErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_provider_error_component import (
        ApiV1SecretmanagerManagersCreateProviderErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_provider_id_error_component import (
        ApiV1SecretmanagerManagersCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_provider_reference_error_component import (
        ApiV1SecretmanagerManagersCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_reconciliation_enabled_error_component import (
        ApiV1SecretmanagerManagersCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_secrets_engines_count_error_component import (
        ApiV1SecretmanagerManagersCreateSecretsEnginesCountErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_sla_availability_error_component import (
        ApiV1SecretmanagerManagersCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_sla_target_error_component import (
        ApiV1SecretmanagerManagersCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_slo_availability_error_component import (
        ApiV1SecretmanagerManagersCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_slo_target_error_component import (
        ApiV1SecretmanagerManagersCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_target_availability_error_component import (
        ApiV1SecretmanagerManagersCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_tolerations_error_component import (
        ApiV1SecretmanagerManagersCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_vault_mode_error_component import (
        ApiV1SecretmanagerManagersCreateVaultModeErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_create_vault_version_error_component import (
        ApiV1SecretmanagerManagersCreateVaultVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1SecretmanagerManagersCreateValidationError")


@_attrs_define
class ApiV1SecretmanagerManagersCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1SecretmanagerManagersCreateAnnotationsErrorComponent |
            ApiV1SecretmanagerManagersCreateArchivedAtErrorComponent |
            ApiV1SecretmanagerManagersCreateArchivedErrorComponent |
            ApiV1SecretmanagerManagersCreateArchivedReasonErrorComponent |
            ApiV1SecretmanagerManagersCreateAuthMethodsCountErrorComponent |
            ApiV1SecretmanagerManagersCreateCredentialErrorComponent |
            ApiV1SecretmanagerManagersCreateCriticalityErrorComponent |
            ApiV1SecretmanagerManagersCreateDebugModeErrorComponent |
            ApiV1SecretmanagerManagersCreateDisplayNameErrorComponent |
            ApiV1SecretmanagerManagersCreateHostnameErrorComponent |
            ApiV1SecretmanagerManagersCreateIsInitializedErrorComponent |
            ApiV1SecretmanagerManagersCreateIsSealedErrorComponent | ApiV1SecretmanagerManagersCreateK8SAppErrorComponent |
            ApiV1SecretmanagerManagersCreateK8SClusterErrorComponent | ApiV1SecretmanagerManagersCreateKindErrorComponent |
            ApiV1SecretmanagerManagersCreateLabelsErrorComponent | ApiV1SecretmanagerManagersCreateMetadataErrorComponent |
            ApiV1SecretmanagerManagersCreateNameErrorComponent |
            ApiV1SecretmanagerManagersCreateNonFieldErrorsErrorComponent |
            ApiV1SecretmanagerManagersCreatePlatformServiceErrorComponent |
            ApiV1SecretmanagerManagersCreatePoliciesCountErrorComponent |
            ApiV1SecretmanagerManagersCreateProviderErrorComponent |
            ApiV1SecretmanagerManagersCreateProviderIdErrorComponent |
            ApiV1SecretmanagerManagersCreateProviderReferenceErrorComponent |
            ApiV1SecretmanagerManagersCreateReconciliationEnabledErrorComponent |
            ApiV1SecretmanagerManagersCreateSecretsEnginesCountErrorComponent |
            ApiV1SecretmanagerManagersCreateSlaAvailabilityErrorComponent |
            ApiV1SecretmanagerManagersCreateSlaTargetErrorComponent |
            ApiV1SecretmanagerManagersCreateSloAvailabilityErrorComponent |
            ApiV1SecretmanagerManagersCreateSloTargetErrorComponent |
            ApiV1SecretmanagerManagersCreateTargetAvailabilityErrorComponent |
            ApiV1SecretmanagerManagersCreateTolerationsErrorComponent |
            ApiV1SecretmanagerManagersCreateVaultModeErrorComponent |
            ApiV1SecretmanagerManagersCreateVaultVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1SecretmanagerManagersCreateAnnotationsErrorComponent
        | ApiV1SecretmanagerManagersCreateArchivedAtErrorComponent
        | ApiV1SecretmanagerManagersCreateArchivedErrorComponent
        | ApiV1SecretmanagerManagersCreateArchivedReasonErrorComponent
        | ApiV1SecretmanagerManagersCreateAuthMethodsCountErrorComponent
        | ApiV1SecretmanagerManagersCreateCredentialErrorComponent
        | ApiV1SecretmanagerManagersCreateCriticalityErrorComponent
        | ApiV1SecretmanagerManagersCreateDebugModeErrorComponent
        | ApiV1SecretmanagerManagersCreateDisplayNameErrorComponent
        | ApiV1SecretmanagerManagersCreateHostnameErrorComponent
        | ApiV1SecretmanagerManagersCreateIsInitializedErrorComponent
        | ApiV1SecretmanagerManagersCreateIsSealedErrorComponent
        | ApiV1SecretmanagerManagersCreateK8SAppErrorComponent
        | ApiV1SecretmanagerManagersCreateK8SClusterErrorComponent
        | ApiV1SecretmanagerManagersCreateKindErrorComponent
        | ApiV1SecretmanagerManagersCreateLabelsErrorComponent
        | ApiV1SecretmanagerManagersCreateMetadataErrorComponent
        | ApiV1SecretmanagerManagersCreateNameErrorComponent
        | ApiV1SecretmanagerManagersCreateNonFieldErrorsErrorComponent
        | ApiV1SecretmanagerManagersCreatePlatformServiceErrorComponent
        | ApiV1SecretmanagerManagersCreatePoliciesCountErrorComponent
        | ApiV1SecretmanagerManagersCreateProviderErrorComponent
        | ApiV1SecretmanagerManagersCreateProviderIdErrorComponent
        | ApiV1SecretmanagerManagersCreateProviderReferenceErrorComponent
        | ApiV1SecretmanagerManagersCreateReconciliationEnabledErrorComponent
        | ApiV1SecretmanagerManagersCreateSecretsEnginesCountErrorComponent
        | ApiV1SecretmanagerManagersCreateSlaAvailabilityErrorComponent
        | ApiV1SecretmanagerManagersCreateSlaTargetErrorComponent
        | ApiV1SecretmanagerManagersCreateSloAvailabilityErrorComponent
        | ApiV1SecretmanagerManagersCreateSloTargetErrorComponent
        | ApiV1SecretmanagerManagersCreateTargetAvailabilityErrorComponent
        | ApiV1SecretmanagerManagersCreateTolerationsErrorComponent
        | ApiV1SecretmanagerManagersCreateVaultModeErrorComponent
        | ApiV1SecretmanagerManagersCreateVaultVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_secretmanager_managers_create_annotations_error_component import (
            ApiV1SecretmanagerManagersCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_archived_at_error_component import (
            ApiV1SecretmanagerManagersCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_archived_error_component import (
            ApiV1SecretmanagerManagersCreateArchivedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_archived_reason_error_component import (
            ApiV1SecretmanagerManagersCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_auth_methods_count_error_component import (
            ApiV1SecretmanagerManagersCreateAuthMethodsCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_credential_error_component import (
            ApiV1SecretmanagerManagersCreateCredentialErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_criticality_error_component import (
            ApiV1SecretmanagerManagersCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_debug_mode_error_component import (
            ApiV1SecretmanagerManagersCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_display_name_error_component import (
            ApiV1SecretmanagerManagersCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_hostname_error_component import (
            ApiV1SecretmanagerManagersCreateHostnameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_is_initialized_error_component import (
            ApiV1SecretmanagerManagersCreateIsInitializedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_is_sealed_error_component import (
            ApiV1SecretmanagerManagersCreateIsSealedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_k8s_app_error_component import (
            ApiV1SecretmanagerManagersCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_k8s_cluster_error_component import (
            ApiV1SecretmanagerManagersCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_kind_error_component import (
            ApiV1SecretmanagerManagersCreateKindErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_labels_error_component import (
            ApiV1SecretmanagerManagersCreateLabelsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_name_error_component import (
            ApiV1SecretmanagerManagersCreateNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_non_field_errors_error_component import (
            ApiV1SecretmanagerManagersCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_platform_service_error_component import (
            ApiV1SecretmanagerManagersCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_policies_count_error_component import (
            ApiV1SecretmanagerManagersCreatePoliciesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_provider_error_component import (
            ApiV1SecretmanagerManagersCreateProviderErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_provider_id_error_component import (
            ApiV1SecretmanagerManagersCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_provider_reference_error_component import (
            ApiV1SecretmanagerManagersCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_reconciliation_enabled_error_component import (
            ApiV1SecretmanagerManagersCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_secrets_engines_count_error_component import (
            ApiV1SecretmanagerManagersCreateSecretsEnginesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_sla_availability_error_component import (
            ApiV1SecretmanagerManagersCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_sla_target_error_component import (
            ApiV1SecretmanagerManagersCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_slo_availability_error_component import (
            ApiV1SecretmanagerManagersCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_slo_target_error_component import (
            ApiV1SecretmanagerManagersCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_target_availability_error_component import (
            ApiV1SecretmanagerManagersCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_tolerations_error_component import (
            ApiV1SecretmanagerManagersCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_vault_mode_error_component import (
            ApiV1SecretmanagerManagersCreateVaultModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_vault_version_error_component import (
            ApiV1SecretmanagerManagersCreateVaultVersionErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateVaultModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateIsSealedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateIsInitializedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateSecretsEnginesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateAuthMethodsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreatePoliciesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateVaultVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersCreateCredentialErrorComponent):
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
        from ..models.api_v1_secretmanager_managers_create_annotations_error_component import (
            ApiV1SecretmanagerManagersCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_archived_at_error_component import (
            ApiV1SecretmanagerManagersCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_archived_error_component import (
            ApiV1SecretmanagerManagersCreateArchivedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_archived_reason_error_component import (
            ApiV1SecretmanagerManagersCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_auth_methods_count_error_component import (
            ApiV1SecretmanagerManagersCreateAuthMethodsCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_credential_error_component import (
            ApiV1SecretmanagerManagersCreateCredentialErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_criticality_error_component import (
            ApiV1SecretmanagerManagersCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_debug_mode_error_component import (
            ApiV1SecretmanagerManagersCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_display_name_error_component import (
            ApiV1SecretmanagerManagersCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_hostname_error_component import (
            ApiV1SecretmanagerManagersCreateHostnameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_is_initialized_error_component import (
            ApiV1SecretmanagerManagersCreateIsInitializedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_is_sealed_error_component import (
            ApiV1SecretmanagerManagersCreateIsSealedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_k8s_app_error_component import (
            ApiV1SecretmanagerManagersCreateK8SAppErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_k8s_cluster_error_component import (
            ApiV1SecretmanagerManagersCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_kind_error_component import (
            ApiV1SecretmanagerManagersCreateKindErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_labels_error_component import (
            ApiV1SecretmanagerManagersCreateLabelsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_metadata_error_component import (
            ApiV1SecretmanagerManagersCreateMetadataErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_name_error_component import (
            ApiV1SecretmanagerManagersCreateNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_non_field_errors_error_component import (
            ApiV1SecretmanagerManagersCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_platform_service_error_component import (
            ApiV1SecretmanagerManagersCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_policies_count_error_component import (
            ApiV1SecretmanagerManagersCreatePoliciesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_provider_error_component import (
            ApiV1SecretmanagerManagersCreateProviderErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_provider_id_error_component import (
            ApiV1SecretmanagerManagersCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_provider_reference_error_component import (
            ApiV1SecretmanagerManagersCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_reconciliation_enabled_error_component import (
            ApiV1SecretmanagerManagersCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_secrets_engines_count_error_component import (
            ApiV1SecretmanagerManagersCreateSecretsEnginesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_sla_availability_error_component import (
            ApiV1SecretmanagerManagersCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_sla_target_error_component import (
            ApiV1SecretmanagerManagersCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_slo_availability_error_component import (
            ApiV1SecretmanagerManagersCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_slo_target_error_component import (
            ApiV1SecretmanagerManagersCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_target_availability_error_component import (
            ApiV1SecretmanagerManagersCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_tolerations_error_component import (
            ApiV1SecretmanagerManagersCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_vault_mode_error_component import (
            ApiV1SecretmanagerManagersCreateVaultModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_create_vault_version_error_component import (
            ApiV1SecretmanagerManagersCreateVaultVersionErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1SecretmanagerManagersCreateAnnotationsErrorComponent
                | ApiV1SecretmanagerManagersCreateArchivedAtErrorComponent
                | ApiV1SecretmanagerManagersCreateArchivedErrorComponent
                | ApiV1SecretmanagerManagersCreateArchivedReasonErrorComponent
                | ApiV1SecretmanagerManagersCreateAuthMethodsCountErrorComponent
                | ApiV1SecretmanagerManagersCreateCredentialErrorComponent
                | ApiV1SecretmanagerManagersCreateCriticalityErrorComponent
                | ApiV1SecretmanagerManagersCreateDebugModeErrorComponent
                | ApiV1SecretmanagerManagersCreateDisplayNameErrorComponent
                | ApiV1SecretmanagerManagersCreateHostnameErrorComponent
                | ApiV1SecretmanagerManagersCreateIsInitializedErrorComponent
                | ApiV1SecretmanagerManagersCreateIsSealedErrorComponent
                | ApiV1SecretmanagerManagersCreateK8SAppErrorComponent
                | ApiV1SecretmanagerManagersCreateK8SClusterErrorComponent
                | ApiV1SecretmanagerManagersCreateKindErrorComponent
                | ApiV1SecretmanagerManagersCreateLabelsErrorComponent
                | ApiV1SecretmanagerManagersCreateMetadataErrorComponent
                | ApiV1SecretmanagerManagersCreateNameErrorComponent
                | ApiV1SecretmanagerManagersCreateNonFieldErrorsErrorComponent
                | ApiV1SecretmanagerManagersCreatePlatformServiceErrorComponent
                | ApiV1SecretmanagerManagersCreatePoliciesCountErrorComponent
                | ApiV1SecretmanagerManagersCreateProviderErrorComponent
                | ApiV1SecretmanagerManagersCreateProviderIdErrorComponent
                | ApiV1SecretmanagerManagersCreateProviderReferenceErrorComponent
                | ApiV1SecretmanagerManagersCreateReconciliationEnabledErrorComponent
                | ApiV1SecretmanagerManagersCreateSecretsEnginesCountErrorComponent
                | ApiV1SecretmanagerManagersCreateSlaAvailabilityErrorComponent
                | ApiV1SecretmanagerManagersCreateSlaTargetErrorComponent
                | ApiV1SecretmanagerManagersCreateSloAvailabilityErrorComponent
                | ApiV1SecretmanagerManagersCreateSloTargetErrorComponent
                | ApiV1SecretmanagerManagersCreateTargetAvailabilityErrorComponent
                | ApiV1SecretmanagerManagersCreateTolerationsErrorComponent
                | ApiV1SecretmanagerManagersCreateVaultModeErrorComponent
                | ApiV1SecretmanagerManagersCreateVaultVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_0 = (
                        ApiV1SecretmanagerManagersCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_1 = (
                        ApiV1SecretmanagerManagersCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_2 = (
                        ApiV1SecretmanagerManagersCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_3 = (
                        ApiV1SecretmanagerManagersCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_4 = (
                        ApiV1SecretmanagerManagersCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_5 = (
                        ApiV1SecretmanagerManagersCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_6 = (
                        ApiV1SecretmanagerManagersCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_7 = (
                        ApiV1SecretmanagerManagersCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_8 = (
                        ApiV1SecretmanagerManagersCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_9 = (
                        ApiV1SecretmanagerManagersCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_10 = (
                        ApiV1SecretmanagerManagersCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_11 = (
                        ApiV1SecretmanagerManagersCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_12 = (
                        ApiV1SecretmanagerManagersCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_13 = (
                        ApiV1SecretmanagerManagersCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_14 = (
                        ApiV1SecretmanagerManagersCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_15 = (
                        ApiV1SecretmanagerManagersCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_16 = (
                        ApiV1SecretmanagerManagersCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_17 = (
                        ApiV1SecretmanagerManagersCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_18 = (
                        ApiV1SecretmanagerManagersCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_19 = (
                        ApiV1SecretmanagerManagersCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_20 = (
                        ApiV1SecretmanagerManagersCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_21 = (
                        ApiV1SecretmanagerManagersCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_22 = (
                        ApiV1SecretmanagerManagersCreateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_23 = (
                        ApiV1SecretmanagerManagersCreateVaultModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_24 = (
                        ApiV1SecretmanagerManagersCreateIsSealedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_25 = (
                        ApiV1SecretmanagerManagersCreateIsInitializedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_26 = (
                        ApiV1SecretmanagerManagersCreateSecretsEnginesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_27 = (
                        ApiV1SecretmanagerManagersCreateAuthMethodsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_28 = (
                        ApiV1SecretmanagerManagersCreatePoliciesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_29 = (
                        ApiV1SecretmanagerManagersCreateVaultVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_30 = (
                        ApiV1SecretmanagerManagersCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_31 = (
                        ApiV1SecretmanagerManagersCreateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_create_error_type_32 = (
                        ApiV1SecretmanagerManagersCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_secretmanager_managers_create_error_type_33 = (
                    ApiV1SecretmanagerManagersCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_secretmanager_managers_create_error_type_33

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_secretmanager_managers_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_secretmanager_managers_create_validation_error.additional_properties = d
        return api_v1_secretmanager_managers_create_validation_error

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
