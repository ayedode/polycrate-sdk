from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_actual_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_addon_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateAddonErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_annotations_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_archived_at_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_archived_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_archived_reason_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_block_config_template_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_block_name_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateBlockNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_criticality_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_debug_mode_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_discovery_enabled_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_display_name_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_k8s_cluster_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_kind_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_labels_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_name_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_non_field_errors_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_order_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateOrderErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_platform_service_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_provider_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_provider_id_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_provider_reference_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_scope_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_sla_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_sla_target_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_slo_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_slo_target_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_target_availability_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_version_error_component import (
        ApiV1KubernetesClusterAddonSubscriptionsCreateVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesClusterAddonSubscriptionsCreateValidationError")


@_attrs_define
class ApiV1KubernetesClusterAddonSubscriptionsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesClusterAddonSubscriptionsCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateAddonErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateAnnotationsErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedAtErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedReasonErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateBlockConfigTemplateErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateBlockNameErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateCriticalityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateDebugModeErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateDisplayNameErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateK8SClusterErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateKindErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateLabelsErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateNameErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateOrderErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreatePlatformServiceErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateProviderErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateProviderIdErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateProviderReferenceErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateScopeErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateSlaTargetErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateSloTargetErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesClusterAddonSubscriptionsCreateVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesClusterAddonSubscriptionsCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateAddonErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateAnnotationsErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedAtErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedReasonErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateBlockConfigTemplateErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateBlockNameErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateCriticalityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateDebugModeErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateDisplayNameErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateK8SClusterErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateKindErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateLabelsErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateNameErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateOrderErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreatePlatformServiceErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateProviderErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateProviderIdErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateProviderReferenceErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateScopeErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateSlaTargetErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateSloTargetErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesClusterAddonSubscriptionsCreateVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_actual_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_addon_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateAddonErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_annotations_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_archived_at_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_archived_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_archived_reason_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_block_config_template_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_block_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateBlockNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_criticality_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_debug_mode_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_discovery_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_display_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_k8s_cluster_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_kind_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_labels_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_non_field_errors_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_platform_service_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_provider_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_provider_id_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_provider_reference_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_scope_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_sla_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_sla_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_slo_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_slo_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_target_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_version_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateVersionErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateProviderReferenceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateDiscoveryEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreatePlatformServiceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedReasonErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateActualAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateSloAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateSlaAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateAddonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateBlockNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClusterAddonSubscriptionsCreateBlockConfigTemplateErrorComponent
            ):
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
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_actual_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_addon_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateAddonErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_annotations_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_archived_at_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_archived_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_archived_reason_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_block_config_template_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_block_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateBlockNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_criticality_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_debug_mode_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_discovery_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_display_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_k8s_cluster_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_kind_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_labels_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_name_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_non_field_errors_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_order_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateOrderErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_platform_service_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_provider_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_provider_id_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_provider_reference_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_scope_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_sla_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_sla_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_slo_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_slo_target_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_target_availability_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_cluster_addon_subscriptions_create_version_error_component import (
            ApiV1KubernetesClusterAddonSubscriptionsCreateVersionErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesClusterAddonSubscriptionsCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateAddonErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateAnnotationsErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedAtErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedReasonErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateBlockConfigTemplateErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateBlockNameErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateCriticalityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateDebugModeErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateDisplayNameErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateK8SClusterErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateKindErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateLabelsErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateNameErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateOrderErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreatePlatformServiceErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateProviderErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateProviderIdErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateProviderReferenceErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateScopeErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateSlaTargetErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateSloTargetErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesClusterAddonSubscriptionsCreateVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_0 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_1 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_2 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_3 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_4 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_5 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_6 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_7 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_8 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_9 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateReconciliationEnabledErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_10 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_11 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_12 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_13 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_14 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_15 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_16 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_17 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_18 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_19 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_20 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_21 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_22 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_23 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_24 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_25 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateAddonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_26 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_27 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateBlockNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_28 = (
                        ApiV1KubernetesClusterAddonSubscriptionsCreateBlockConfigTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_29 = (
                    ApiV1KubernetesClusterAddonSubscriptionsCreateOrderErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_cluster_addon_subscriptions_create_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_cluster_addon_subscriptions_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_cluster_addon_subscriptions_create_validation_error.additional_properties = d
        return api_v1_kubernetes_cluster_addon_subscriptions_create_validation_error

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
