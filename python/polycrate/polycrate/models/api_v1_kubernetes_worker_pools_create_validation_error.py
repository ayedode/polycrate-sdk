from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_worker_pools_create_actual_availability_error_component import (
        ApiV1KubernetesWorkerPoolsCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_annotations_error_component import (
        ApiV1KubernetesWorkerPoolsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_archived_at_error_component import (
        ApiV1KubernetesWorkerPoolsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_archived_error_component import (
        ApiV1KubernetesWorkerPoolsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_archived_reason_error_component import (
        ApiV1KubernetesWorkerPoolsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_controlplane_id_error_component import (
        ApiV1KubernetesWorkerPoolsCreateControlplaneIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_criticality_error_component import (
        ApiV1KubernetesWorkerPoolsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_debug_mode_error_component import (
        ApiV1KubernetesWorkerPoolsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_desired_count_error_component import (
        ApiV1KubernetesWorkerPoolsCreateDesiredCountErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_discovery_enabled_error_component import (
        ApiV1KubernetesWorkerPoolsCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_display_name_error_component import (
        ApiV1KubernetesWorkerPoolsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_hardening_enabled_error_component import (
        ApiV1KubernetesWorkerPoolsCreateHardeningEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_image_error_component import (
        ApiV1KubernetesWorkerPoolsCreateImageErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_kind_error_component import (
        ApiV1KubernetesWorkerPoolsCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_labels_error_component import (
        ApiV1KubernetesWorkerPoolsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_location_error_component import (
        ApiV1KubernetesWorkerPoolsCreateLocationErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_name_error_component import (
        ApiV1KubernetesWorkerPoolsCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_non_field_errors_error_component import (
        ApiV1KubernetesWorkerPoolsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_platform_service_error_component import (
        ApiV1KubernetesWorkerPoolsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_product_id_error_component import (
        ApiV1KubernetesWorkerPoolsCreateProductIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_provider_account_id_error_component import (
        ApiV1KubernetesWorkerPoolsCreateProviderAccountIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_provider_error_component import (
        ApiV1KubernetesWorkerPoolsCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_provider_id_error_component import (
        ApiV1KubernetesWorkerPoolsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_provider_reference_error_component import (
        ApiV1KubernetesWorkerPoolsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesWorkerPoolsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_scope_error_component import (
        ApiV1KubernetesWorkerPoolsCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_sla_availability_error_component import (
        ApiV1KubernetesWorkerPoolsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_sla_target_error_component import (
        ApiV1KubernetesWorkerPoolsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_slo_availability_error_component import (
        ApiV1KubernetesWorkerPoolsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_slo_target_error_component import (
        ApiV1KubernetesWorkerPoolsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_ssh_key_credential_id_error_component import (
        ApiV1KubernetesWorkerPoolsCreateSshKeyCredentialIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_create_target_availability_error_component import (
        ApiV1KubernetesWorkerPoolsCreateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesWorkerPoolsCreateValidationError")


@_attrs_define
class ApiV1KubernetesWorkerPoolsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesWorkerPoolsCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateAnnotationsErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateArchivedAtErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateArchivedErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateArchivedReasonErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateControlplaneIdErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateCriticalityErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateDebugModeErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateDesiredCountErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateDisplayNameErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateHardeningEnabledErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateImageErrorComponent | ApiV1KubernetesWorkerPoolsCreateKindErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateLabelsErrorComponent | ApiV1KubernetesWorkerPoolsCreateLocationErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateNameErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesWorkerPoolsCreatePlatformServiceErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateProductIdErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateProviderAccountIdErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateProviderErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateProviderIdErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateProviderReferenceErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateScopeErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateSlaTargetErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateSloTargetErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateSshKeyCredentialIdErrorComponent |
            ApiV1KubernetesWorkerPoolsCreateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesWorkerPoolsCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateAnnotationsErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateArchivedAtErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateArchivedErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateArchivedReasonErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateControlplaneIdErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateCriticalityErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateDebugModeErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateDesiredCountErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateDisplayNameErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateHardeningEnabledErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateImageErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateKindErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateLabelsErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateLocationErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateNameErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesWorkerPoolsCreatePlatformServiceErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateProductIdErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateProviderAccountIdErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateProviderErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateProviderIdErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateProviderReferenceErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateScopeErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateSlaTargetErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateSloTargetErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateSshKeyCredentialIdErrorComponent
        | ApiV1KubernetesWorkerPoolsCreateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_worker_pools_create_actual_availability_error_component import (
            ApiV1KubernetesWorkerPoolsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_annotations_error_component import (
            ApiV1KubernetesWorkerPoolsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_archived_at_error_component import (
            ApiV1KubernetesWorkerPoolsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_archived_error_component import (
            ApiV1KubernetesWorkerPoolsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_archived_reason_error_component import (
            ApiV1KubernetesWorkerPoolsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_controlplane_id_error_component import (
            ApiV1KubernetesWorkerPoolsCreateControlplaneIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_criticality_error_component import (
            ApiV1KubernetesWorkerPoolsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_debug_mode_error_component import (
            ApiV1KubernetesWorkerPoolsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_desired_count_error_component import (
            ApiV1KubernetesWorkerPoolsCreateDesiredCountErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_discovery_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_display_name_error_component import (
            ApiV1KubernetesWorkerPoolsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_image_error_component import (
            ApiV1KubernetesWorkerPoolsCreateImageErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_kind_error_component import (
            ApiV1KubernetesWorkerPoolsCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_labels_error_component import (
            ApiV1KubernetesWorkerPoolsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_location_error_component import (
            ApiV1KubernetesWorkerPoolsCreateLocationErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_name_error_component import (
            ApiV1KubernetesWorkerPoolsCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_non_field_errors_error_component import (
            ApiV1KubernetesWorkerPoolsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_platform_service_error_component import (
            ApiV1KubernetesWorkerPoolsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_product_id_error_component import (
            ApiV1KubernetesWorkerPoolsCreateProductIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_provider_account_id_error_component import (
            ApiV1KubernetesWorkerPoolsCreateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_provider_error_component import (
            ApiV1KubernetesWorkerPoolsCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_provider_id_error_component import (
            ApiV1KubernetesWorkerPoolsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_provider_reference_error_component import (
            ApiV1KubernetesWorkerPoolsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_scope_error_component import (
            ApiV1KubernetesWorkerPoolsCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_sla_availability_error_component import (
            ApiV1KubernetesWorkerPoolsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_sla_target_error_component import (
            ApiV1KubernetesWorkerPoolsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_slo_availability_error_component import (
            ApiV1KubernetesWorkerPoolsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_slo_target_error_component import (
            ApiV1KubernetesWorkerPoolsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_ssh_key_credential_id_error_component import (
            ApiV1KubernetesWorkerPoolsCreateSshKeyCredentialIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_target_availability_error_component import (
            ApiV1KubernetesWorkerPoolsCreateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateControlplaneIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateProviderAccountIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateProductIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateDesiredCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateImageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateLocationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsCreateSshKeyCredentialIdErrorComponent):
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
        from ..models.api_v1_kubernetes_worker_pools_create_actual_availability_error_component import (
            ApiV1KubernetesWorkerPoolsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_annotations_error_component import (
            ApiV1KubernetesWorkerPoolsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_archived_at_error_component import (
            ApiV1KubernetesWorkerPoolsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_archived_error_component import (
            ApiV1KubernetesWorkerPoolsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_archived_reason_error_component import (
            ApiV1KubernetesWorkerPoolsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_controlplane_id_error_component import (
            ApiV1KubernetesWorkerPoolsCreateControlplaneIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_criticality_error_component import (
            ApiV1KubernetesWorkerPoolsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_debug_mode_error_component import (
            ApiV1KubernetesWorkerPoolsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_desired_count_error_component import (
            ApiV1KubernetesWorkerPoolsCreateDesiredCountErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_discovery_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_display_name_error_component import (
            ApiV1KubernetesWorkerPoolsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_hardening_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsCreateHardeningEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_image_error_component import (
            ApiV1KubernetesWorkerPoolsCreateImageErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_kind_error_component import (
            ApiV1KubernetesWorkerPoolsCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_labels_error_component import (
            ApiV1KubernetesWorkerPoolsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_location_error_component import (
            ApiV1KubernetesWorkerPoolsCreateLocationErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_name_error_component import (
            ApiV1KubernetesWorkerPoolsCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_non_field_errors_error_component import (
            ApiV1KubernetesWorkerPoolsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_platform_service_error_component import (
            ApiV1KubernetesWorkerPoolsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_product_id_error_component import (
            ApiV1KubernetesWorkerPoolsCreateProductIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_provider_account_id_error_component import (
            ApiV1KubernetesWorkerPoolsCreateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_provider_error_component import (
            ApiV1KubernetesWorkerPoolsCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_provider_id_error_component import (
            ApiV1KubernetesWorkerPoolsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_provider_reference_error_component import (
            ApiV1KubernetesWorkerPoolsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_scope_error_component import (
            ApiV1KubernetesWorkerPoolsCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_sla_availability_error_component import (
            ApiV1KubernetesWorkerPoolsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_sla_target_error_component import (
            ApiV1KubernetesWorkerPoolsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_slo_availability_error_component import (
            ApiV1KubernetesWorkerPoolsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_slo_target_error_component import (
            ApiV1KubernetesWorkerPoolsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_ssh_key_credential_id_error_component import (
            ApiV1KubernetesWorkerPoolsCreateSshKeyCredentialIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_create_target_availability_error_component import (
            ApiV1KubernetesWorkerPoolsCreateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesWorkerPoolsCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateAnnotationsErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateArchivedAtErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateArchivedErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateArchivedReasonErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateControlplaneIdErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateCriticalityErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateDebugModeErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateDesiredCountErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateDisplayNameErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateHardeningEnabledErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateImageErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateKindErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateLabelsErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateLocationErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateNameErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesWorkerPoolsCreatePlatformServiceErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateProductIdErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateProviderAccountIdErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateProviderErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateProviderIdErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateProviderReferenceErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateScopeErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateSlaTargetErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateSloTargetErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateSshKeyCredentialIdErrorComponent
                | ApiV1KubernetesWorkerPoolsCreateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_0 = (
                        ApiV1KubernetesWorkerPoolsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_1 = (
                        ApiV1KubernetesWorkerPoolsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_2 = (
                        ApiV1KubernetesWorkerPoolsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_3 = (
                        ApiV1KubernetesWorkerPoolsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_4 = (
                        ApiV1KubernetesWorkerPoolsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_5 = (
                        ApiV1KubernetesWorkerPoolsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_6 = (
                        ApiV1KubernetesWorkerPoolsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_7 = (
                        ApiV1KubernetesWorkerPoolsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_8 = (
                        ApiV1KubernetesWorkerPoolsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_9 = (
                        ApiV1KubernetesWorkerPoolsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_10 = (
                        ApiV1KubernetesWorkerPoolsCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_11 = (
                        ApiV1KubernetesWorkerPoolsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_12 = (
                        ApiV1KubernetesWorkerPoolsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_13 = (
                        ApiV1KubernetesWorkerPoolsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_14 = (
                        ApiV1KubernetesWorkerPoolsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_15 = (
                        ApiV1KubernetesWorkerPoolsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_16 = (
                        ApiV1KubernetesWorkerPoolsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_17 = (
                        ApiV1KubernetesWorkerPoolsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_18 = (
                        ApiV1KubernetesWorkerPoolsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_19 = (
                        ApiV1KubernetesWorkerPoolsCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_20 = (
                        ApiV1KubernetesWorkerPoolsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_21 = (
                        ApiV1KubernetesWorkerPoolsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_22 = (
                        ApiV1KubernetesWorkerPoolsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_23 = (
                        ApiV1KubernetesWorkerPoolsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_24 = (
                        ApiV1KubernetesWorkerPoolsCreateControlplaneIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_25 = (
                        ApiV1KubernetesWorkerPoolsCreateProviderAccountIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_26 = (
                        ApiV1KubernetesWorkerPoolsCreateProductIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_27 = (
                        ApiV1KubernetesWorkerPoolsCreateDesiredCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_28 = (
                        ApiV1KubernetesWorkerPoolsCreateImageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_29 = (
                        ApiV1KubernetesWorkerPoolsCreateLocationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_30 = (
                        ApiV1KubernetesWorkerPoolsCreateSshKeyCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_31 = (
                    ApiV1KubernetesWorkerPoolsCreateHardeningEnabledErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_worker_pools_create_error_type_31

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_worker_pools_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_worker_pools_create_validation_error.additional_properties = d
        return api_v1_kubernetes_worker_pools_create_validation_error

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
