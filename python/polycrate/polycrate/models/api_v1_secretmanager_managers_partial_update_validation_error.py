from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_secretmanager_managers_partial_update_annotations_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_archived_at_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_archived_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_archived_reason_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_auth_methods_count_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateAuthMethodsCountErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_credential_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateCredentialErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_criticality_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_debug_mode_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_display_name_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_hostname_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateHostnameErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_is_initialized_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateIsInitializedErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_is_sealed_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateIsSealedErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_k8s_app_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateK8SAppErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_k8s_cluster_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_kind_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_labels_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_metadata_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_name_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_non_field_errors_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_platform_service_error_component import (
        ApiV1SecretmanagerManagersPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_policies_count_error_component import (
        ApiV1SecretmanagerManagersPartialUpdatePoliciesCountErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_provider_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_provider_id_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_provider_reference_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_reconciliation_enabled_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_secrets_engines_count_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateSecretsEnginesCountErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_sla_availability_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_sla_target_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_slo_availability_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_slo_target_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_target_availability_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_tolerations_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_vault_mode_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateVaultModeErrorComponent,
    )
    from ..models.api_v1_secretmanager_managers_partial_update_vault_version_error_component import (
        ApiV1SecretmanagerManagersPartialUpdateVaultVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1SecretmanagerManagersPartialUpdateValidationError")


@_attrs_define
class ApiV1SecretmanagerManagersPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1SecretmanagerManagersPartialUpdateAnnotationsErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateArchivedAtErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateArchivedErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateArchivedReasonErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateAuthMethodsCountErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateCredentialErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateCriticalityErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateDebugModeErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateDisplayNameErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateHostnameErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateIsInitializedErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateIsSealedErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateK8SAppErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateK8SClusterErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateKindErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateLabelsErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateMetadataErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateNameErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdatePlatformServiceErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdatePoliciesCountErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateProviderErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateProviderIdErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateProviderReferenceErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateSecretsEnginesCountErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateSlaTargetErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateSloAvailabilityErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateSloTargetErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateTolerationsErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateVaultModeErrorComponent |
            ApiV1SecretmanagerManagersPartialUpdateVaultVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1SecretmanagerManagersPartialUpdateAnnotationsErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateArchivedAtErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateArchivedErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateArchivedReasonErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateAuthMethodsCountErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateCredentialErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateCriticalityErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateDebugModeErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateDisplayNameErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateHostnameErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateIsInitializedErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateIsSealedErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateK8SAppErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateK8SClusterErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateKindErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateLabelsErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateMetadataErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateNameErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdatePlatformServiceErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdatePoliciesCountErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateProviderErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateProviderIdErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateProviderReferenceErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateSecretsEnginesCountErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateSlaTargetErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateSloAvailabilityErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateSloTargetErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateTolerationsErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateVaultModeErrorComponent
        | ApiV1SecretmanagerManagersPartialUpdateVaultVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_secretmanager_managers_partial_update_annotations_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_archived_at_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_archived_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_archived_reason_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_auth_methods_count_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateAuthMethodsCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_credential_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_criticality_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_debug_mode_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_display_name_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_hostname_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_is_initialized_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateIsInitializedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_is_sealed_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateIsSealedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_k8s_app_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateK8SAppErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_k8s_cluster_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_kind_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_labels_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_name_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_non_field_errors_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_platform_service_error_component import (
            ApiV1SecretmanagerManagersPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_policies_count_error_component import (
            ApiV1SecretmanagerManagersPartialUpdatePoliciesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_provider_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_provider_id_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_provider_reference_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_reconciliation_enabled_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_secrets_engines_count_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateSecretsEnginesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_sla_availability_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_sla_target_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_slo_availability_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_slo_target_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_target_availability_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_tolerations_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_vault_mode_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateVaultModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_vault_version_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateVaultVersionErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1SecretmanagerManagersPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateVaultModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateIsSealedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateIsInitializedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateSecretsEnginesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateAuthMethodsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdatePoliciesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateVaultVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1SecretmanagerManagersPartialUpdateCredentialErrorComponent):
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
        from ..models.api_v1_secretmanager_managers_partial_update_annotations_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_archived_at_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_archived_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_archived_reason_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_auth_methods_count_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateAuthMethodsCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_credential_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_criticality_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_debug_mode_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_display_name_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_hostname_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_is_initialized_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateIsInitializedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_is_sealed_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateIsSealedErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_k8s_app_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateK8SAppErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_k8s_cluster_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_kind_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_labels_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_metadata_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_name_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_non_field_errors_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_platform_service_error_component import (
            ApiV1SecretmanagerManagersPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_policies_count_error_component import (
            ApiV1SecretmanagerManagersPartialUpdatePoliciesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_provider_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_provider_id_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_provider_reference_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_reconciliation_enabled_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_secrets_engines_count_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateSecretsEnginesCountErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_sla_availability_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_sla_target_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_slo_availability_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_slo_target_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_target_availability_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_tolerations_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_vault_mode_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateVaultModeErrorComponent,
        )
        from ..models.api_v1_secretmanager_managers_partial_update_vault_version_error_component import (
            ApiV1SecretmanagerManagersPartialUpdateVaultVersionErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1SecretmanagerManagersPartialUpdateAnnotationsErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateArchivedAtErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateArchivedErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateArchivedReasonErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateAuthMethodsCountErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateCredentialErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateCriticalityErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateDebugModeErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateDisplayNameErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateHostnameErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateIsInitializedErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateIsSealedErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateK8SAppErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateK8SClusterErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateKindErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateLabelsErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateMetadataErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateNameErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdatePlatformServiceErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdatePoliciesCountErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateProviderErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateProviderIdErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateProviderReferenceErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateSecretsEnginesCountErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateSlaTargetErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateSloAvailabilityErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateSloTargetErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateTolerationsErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateVaultModeErrorComponent
                | ApiV1SecretmanagerManagersPartialUpdateVaultVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_0 = (
                        ApiV1SecretmanagerManagersPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_1 = (
                        ApiV1SecretmanagerManagersPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_2 = (
                        ApiV1SecretmanagerManagersPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_3 = (
                        ApiV1SecretmanagerManagersPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_4 = (
                        ApiV1SecretmanagerManagersPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_5 = (
                        ApiV1SecretmanagerManagersPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_6 = (
                        ApiV1SecretmanagerManagersPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_7 = (
                        ApiV1SecretmanagerManagersPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_8 = (
                        ApiV1SecretmanagerManagersPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_9 = (
                        ApiV1SecretmanagerManagersPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_10 = (
                        ApiV1SecretmanagerManagersPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_11 = (
                        ApiV1SecretmanagerManagersPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_12 = (
                        ApiV1SecretmanagerManagersPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_13 = (
                        ApiV1SecretmanagerManagersPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_14 = (
                        ApiV1SecretmanagerManagersPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_15 = (
                        ApiV1SecretmanagerManagersPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_16 = (
                        ApiV1SecretmanagerManagersPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_17 = (
                        ApiV1SecretmanagerManagersPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_18 = (
                        ApiV1SecretmanagerManagersPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_19 = (
                        ApiV1SecretmanagerManagersPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_20 = (
                        ApiV1SecretmanagerManagersPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_21 = (
                        ApiV1SecretmanagerManagersPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_22 = (
                        ApiV1SecretmanagerManagersPartialUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_23 = (
                        ApiV1SecretmanagerManagersPartialUpdateVaultModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_24 = (
                        ApiV1SecretmanagerManagersPartialUpdateIsSealedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_25 = (
                        ApiV1SecretmanagerManagersPartialUpdateIsInitializedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_26 = (
                        ApiV1SecretmanagerManagersPartialUpdateSecretsEnginesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_27 = (
                        ApiV1SecretmanagerManagersPartialUpdateAuthMethodsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_28 = (
                        ApiV1SecretmanagerManagersPartialUpdatePoliciesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_29 = (
                        ApiV1SecretmanagerManagersPartialUpdateVaultVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_30 = (
                        ApiV1SecretmanagerManagersPartialUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_31 = (
                        ApiV1SecretmanagerManagersPartialUpdateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_32 = (
                        ApiV1SecretmanagerManagersPartialUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_33 = (
                    ApiV1SecretmanagerManagersPartialUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_secretmanager_managers_partial_update_error_type_33

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_secretmanager_managers_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_secretmanager_managers_partial_update_validation_error.additional_properties = d
        return api_v1_secretmanager_managers_partial_update_validation_error

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
